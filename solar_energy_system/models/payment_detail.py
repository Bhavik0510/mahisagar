from odoo import models, fields, api

class PaymentDetail(models.Model):
    _name = 'payment.detail'
    _description = 'Payment Detail'

    sr_no = fields.Integer(string="SR NO")
    dealer_name = fields.Char(string="DEALER NAME")
    customer_name = fields.Char(string="CUSTOMER NAME")
    address = fields.Text(string="ADDRESS")
    consumer_number = fields.Char(string="CONSUMER NUMBER")
    capacity = fields.Float(string="CAPACITY")
    consumer_mobile = fields.Char(string="CONSUMER MOBILE NUMBER")
    discom = fields.Char(string="DISCOM")
    estimate_amount = fields.Float(string="ESTIMATE AMOUNT")
    estimate_paid_date = fields.Date(string="ESTIMATE PAID DATE")
    deal_amount = fields.Float(string="DEAL AMOUNT")
    payment_1 = fields.Integer(string="PAYMENT 1")
    mode_1 = fields.Char(string="MODE")
    date_1 = fields.Date(string="DATE")
    payment_2 = fields.Integer(string="PAYMENT 2")
    mode_2 = fields.Char(string="MODE")
    date_2 = fields.Date(string="DATE")
    total_payment = fields.Integer(string="TOTAL PAYMENT")
    outstanding_amount = fields.Integer(string="OUTSTANDING AMOUNT")
    invoice_number = fields.Char(string="Invoice Number")

    @api.model
    def create_payment_detail(self):
        Invoice = self.env['account.move']
        PaymentDetail = self.env['payment.detail']
        ProjectTask = self.env['project.task']

        invoices = Invoice.search([
            ('move_type', '=', 'out_invoice'),
            ('state', '=', 'posted')
        ])

        last_record = self.env['payment.detail'].search([], order='sr_no desc', limit=1)
        sr_no = last_record.sr_no + 1 if last_record else 1
        created_count = 0

        for inv in invoices:
            existing = PaymentDetail.search([('invoice_number', '=', inv.name)], limit=1)
            if existing:
                continue

            customer = inv.partner_id
            customer_name = customer.name

            task = ProjectTask.search([('partner_id', '=', customer.id)], limit=1)

            dealer_name = task.dealer if task else ''
            consumer_number = task.consumer_no_mis if task else ''
            capacity = task.pv_capacity_kw if task else 0
            consumer_mobile = task.mobile_no_mis if task else ''
            discom = task.discom_name if task else ''
            # deal_amount = task.deal_value if task else inv.amount_total
            deal_amount = inv.amount_total

            address = ', '.join(filter(None, [
                customer.street,
                customer.street2,
                customer.city,
                customer.state_id.name if customer.state_id else '',
                customer.zip,
                customer.country_id.name if customer.country_id else '',
            ]))

            payments = inv._get_reconciled_payments()
            payment_list = []
            total_paid = 0

            for payment in payments:
                payment_list.append({
                    'amount': int(payment.amount),
                    'mode': payment.journal_id.name,
                    'date': payment.date
                })
                total_paid += int(payment.amount)

            # First 2 payments
            payment_1 = payment_list[0]['amount'] if len(payment_list) > 0 else 0
            mode_1 = payment_list[0]['mode'] if len(payment_list) > 0 else ''
            date_1 = payment_list[0]['date'] if len(payment_list) > 0 else False

            payment_2 = payment_list[1]['amount'] if len(payment_list) > 1 else 0
            mode_2 = payment_list[1]['mode'] if len(payment_list) > 1 else ''
            date_2 = payment_list[1]['date'] if len(payment_list) > 1 else False

            outstanding = int(inv.amount_total - total_paid)

            PaymentDetail.create({
                'sr_no': sr_no,
                'invoice_number': inv.name,  # ✅ Save invoice number
                'customer_name': customer_name,
                'dealer_name': dealer_name,
                'address': address,
                'consumer_number': consumer_number,
                'capacity': capacity,
                'consumer_mobile': consumer_mobile,
                'discom': discom,
                'deal_amount': deal_amount,
                'payment_1': payment_1,
                'mode_1': mode_1,
                'date_1': date_1,
                'payment_2': payment_2,
                'mode_2': mode_2,
                'date_2': date_2,
                'total_payment': total_paid,
                'outstanding_amount': outstanding,
            })

            sr_no += 1
            created_count += 1

        return True
