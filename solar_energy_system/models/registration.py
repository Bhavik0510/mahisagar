from odoo import models, fields, api

class RegistrationDetail(models.Model):
    _name = 'registration.detail'
    _description = 'Registration Detail'

    sr_no = fields.Integer(string="SR NO")
    dealer_name = fields.Char(string="DEALER NAME")
    registration_date = fields.Date(string="REGISTRATION DATE")
    customer_name = fields.Char(string="CUSTOMER NAME")
    address = fields.Text(string="ADDRESS")
    sho = fields.Integer(string="SHO")
    consumer_number = fields.Char(string="CONSUMER NUMBER")
    capacity = fields.Float(string="CAPACITY")
    consumer_mobile = fields.Char(string="CONSUMER MOBILE NUMBER")
    discom = fields.Char(string="DISCOM")
    division = fields.Char(string="DIVISION")
    application_no = fields.Char(string="APPLICATION NO")
    feasibility_no = fields.Char(string="FEASIBILITY NO")
    consumer_email_id = fields.Char(string="CONSUMER EMAIL ID")
    invoice_number = fields.Char(string="Invoice Number")

    @api.model
    def create_registration_detail(self):
        Invoice = self.env['account.move']
        Registration = self.env['registration.detail']
        ProjectTask = self.env['project.task']

        invoices = Invoice.search([
            ('move_type', '=', 'out_invoice'),
            ('state', '=', 'posted')
        ])

        last_record = self.env['registration.detail'].search([], order='sr_no desc', limit=1)
        sr_no = last_record.sr_no + 1 if last_record else 1

        for inv in invoices:
            existing = Registration.search([('invoice_number', '=', inv.name)], limit=1)
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
            division = task.division_name if task else ''
            application_no = task.application_number if task else ''

            address = ', '.join(filter(None, [
                customer.street,
                customer.street2,
                customer.city,
                customer.state_id.name if customer.state_id else '',
                customer.zip,
                customer.country_id.name if customer.country_id else '',
            ]))

            Registration.create({
                'sr_no': sr_no,
                'invoice_number': inv.name,
                'dealer_name': dealer_name,
                'customer_name': customer_name,
                'address': address,
                'consumer_number': consumer_number,
                'capacity': capacity,
                'consumer_mobile': consumer_mobile,
                'discom': discom,
                'division': division,
                'application_no': application_no
            })

            sr_no += 1  # Increase for next record

        return True