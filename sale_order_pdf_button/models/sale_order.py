from email.policy import default

from odoo import models, fields,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def print_custom_report(self):
        return self.env.ref('sale_order_pdf_button.custom_sale_order_report').report_action(self)

    x_custom_logo = fields.Binary(string="Custom Logo")

    def print_custom_report_proposal(self):
        return self.env.ref('sale_order_pdf_button.custom_sale_order_proposal_report').report_action(self)

    solar_modules = fields.Text()
    # solar_panel = fields.Text()
    acdb_dcdb = fields.Text()
    # ogs_inverter = fields.Text()
    solar_string_inverter = fields.Text()
    acdc_cable_protected = fields.Text()
    la_cable = fields.Text()
    earthing_cable = fields.Text()
    pipe = fields.Text()
    earthing_system_rods = fields.Text()

    qty_solar_modules = fields.Text()
    qty_acdb_dcdb = fields.Text(default="1 NOS")
    qty_solar_string_inverter = fields.Text(default="1 NOS")
    qty_acdc_cable_protected = fields.Text(default="As Per Design")
    qty_la_cable = fields.Text(default="As Per Design")
    qty_earthing_cable = fields.Text(default="As Per Design")
    qty_pipe = fields.Text(default="As Per Design")
    qty_earthing_system_rods = fields.Text(default="As per Design")

    # brand_make_solar_modules = fields.Text()
    brand_make_solar_modules = fields.Selection([
        ('530_to_550_wp', '530 TO 550 WP'),
        ('600_to_620_wp', '600 TO 620 WP'),
    ], string="Solar Module")
    brand_make_acdb_dcdb = fields.Text(default="Havells / Standard")
    brand_make_solar_string_inverter = fields.Text(default="Solaruaan / Polucab")
    brand_make_acdc_cable_protected = fields.Text(default="Polucab")
    brand_make_la_cable = fields.Text(default="Kanberu / Other")
    brand_make_earthing_cable = fields.Text(default="Kanberu / Other")
    brand_make_pipe = fields.Text(default="Standard")
    brand_make_earthing_system_rods = fields.Text(default="Standard")

    capacity = fields.Float()
    capacity_total = fields.Text()
    meter_charge = fields.Text(default="Including")
    elevated_cost = fields.Text(default="Including")
    geda_charges = fields.Text()
    total_payable_amount = fields.Float()
    pmsg_bank_account = fields.Float()
    final_cost = fields.Float()


    @api.onchange('total_payable_amount', 'pmsg_bank_account')
    def _compute_total(self):
        for rec in self:
            rec.final_cost = rec.total_payable_amount - rec.pmsg_bank_account

    @api.onchange('brand_make_solar_modules', 'capacity')
    def _onchange_capacity_set_price(self):
        self.total_payable_amount = 0

        if self.brand_make_solar_modules == '530_to_550_wp':

            if self.capacity <= 2.17:
                self.total_payable_amount = 0
                self.pmsg_bank_account = 0

            if self.capacity >= 2.18 and self.capacity <= 2.71:
                self.total_payable_amount = 113290
                self.pmsg_bank_account = 63240

            if self.capacity >= 2.72 and self.capacity <= 3.26:
                self.total_payable_amount = 133000
                self.pmsg_bank_account = 73050

            if self.capacity >= 3.27 and self.capacity <= 3.80:
                self.total_payable_amount = 160000
                self.pmsg_bank_account = 78000

            if self.capacity >= 3.81 and self.capacity <= 4.35:
                self.total_payable_amount = 180000
                self.pmsg_bank_account = 78000

            if self.capacity >= 4.36 and self.capacity <= 4.8:
                self.total_payable_amount = 210000
                self.pmsg_bank_account = 78000

            if self.capacity >= 4.9 and self.capacity <= 5.46:
                self.total_payable_amount = 240000
                self.pmsg_bank_account = 78000

            if self.capacity >= 5.46 and self.capacity <= 5.98:
                self.total_payable_amount = 260000
                self.pmsg_bank_account = 78000

            if self.capacity >= 5.99 and self.capacity <= 7.07:
                self.total_payable_amount = 278000
                self.pmsg_bank_account = 78000

            if self.capacity >= 7.08 and self.capacity <= 7.62:
                self.total_payable_amount = 350000
                self.pmsg_bank_account = 78000

            if self.capacity >= 7.63 and self.capacity <= 8.16:
                self.total_payable_amount = 373000
                self.pmsg_bank_account = 78000

            if self.capacity >= 8.17 and self.capacity <= 9.80:
                self.total_payable_amount = 400000
                self.pmsg_bank_account = 78000

            if self.capacity >= 9.81:
                self.total_payable_amount = 460000
                self.pmsg_bank_account = 78000

        if self.brand_make_solar_modules == '600_to_620_wp':

            if self.capacity <= 2.45:
                self.total_payable_amount = 0
                self.pmsg_bank_account = 0

            if self.capacity >= 2.46 and self.capacity <= 3.06:
                self.total_payable_amount = 125000
                self.pmsg_bank_account = 68280

            if self.capacity >= 3.07 and self.capacity <= 3.68:
                self.total_payable_amount = 158000
                self.pmsg_bank_account = 78000

            if self.capacity >= 3.69 and self.capacity <= 4.2:
                self.total_payable_amount = 181000
                self.pmsg_bank_account = 78000

            if self.capacity >= 4.3 and self.capacity <= 4.91:
                self.total_payable_amount = 215000
                self.pmsg_bank_account = 78000

            if self.capacity >= 4.92 and self.capacity <= 5.52:
                self.total_payable_amount = 242000
                self.pmsg_bank_account = 78000

            if self.capacity >= 5.53 and self.capacity <= 6.75:
                self.total_payable_amount = 275000
                self.pmsg_bank_account = 78000

            if self.capacity >= 6.76 and self.capacity <= 7.37:
                self.total_payable_amount = 355000
                self.pmsg_bank_account = 78000

            if self.capacity >= 7.38 and self.capacity <= 7.98:
                self.total_payable_amount = 380000
                self.pmsg_bank_account = 78000

            if self.capacity >= 7.99 and self.capacity <= 9.83:
                self.total_payable_amount = 400000
                self.pmsg_bank_account = 78000

            if self.capacity >= 9.84:
                self.total_payable_amount = 478000
                self.pmsg_bank_account = 78000

