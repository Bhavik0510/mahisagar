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
    acdb_dcdb = fields.Text()
    ogs_inverter = fields.Text()
    acdc_cable_protected = fields.Text()
    la_cable = fields.Text()
    earthing_cable = fields.Text()
    pipe = fields.Text()
    earthing_system_rods = fields.Text()

    qty_solar_modules = fields.Text()
    qty_acdb_dcdb = fields.Text()
    qty_ogs_inverter = fields.Text()
    qty_acdc_cable_protected = fields.Text()
    qty_la_cable = fields.Text()
    qty_earthing_cable = fields.Text()
    qty_pipe = fields.Text()
    qty_earthing_system_rods = fields.Text()

    brand_make_solar_modules = fields.Text()
    brand_make_acdb_dcdb = fields.Text()
    brand_make_ogs_inverter = fields.Text()
    brand_make_acdc_cable_protected = fields.Text()
    brand_make_la_cable = fields.Text()
    brand_make_earthing_cable = fields.Text()
    brand_make_pipe = fields.Text()
    brand_make_earthing_system_rods = fields.Text()

    capacity = fields.Text()
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