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
    # brand_make_solar_modules = fields.Selection([
    #     ('530_to_550_wp', 'ADANI BIFACIAL SOLAR 530 TO 550 WP'),
    #     ('600_to_620_wp', 'ADANI TOPCON SOLAR 600 TO 620 WP'),
    # ], string="Solar Module")
    brand_make_solar_modules_id = fields.Many2one(
        'solar.pv.module',
        string="Solar Module"
    )
    brand_make_acdb_dcdb = fields.Text(default="Havells / Standard")
    brand_make_solar_string_inverter_1 = fields.Text(default="Solaryaan / Polycab")
    brand_make_acdc_cable_protected_ = fields.Text(default="Polycab")
    brand_make_la_cable_ = fields.Text(default="Kanbery / Other")
    brand_make_earthing_cable_ = fields.Text(default="Kanbery / Other")
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

    @api.onchange('brand_make_solar_modules_id', 'capacity')
    def _onchange_solar_module_capacity(self):
        for rec in self:
            if rec.brand_make_solar_modules_id and rec.capacity:
                lines = rec.brand_make_solar_modules_id.line_ids.sorted(key=lambda r: r.capacity)

                matching_line = None
                for i, line in enumerate(lines):
                    if i == len(lines) - 1 or rec.capacity < lines[i + 1].capacity:
                        matching_line = line
                        break

                if matching_line:
                    rec.total_payable_amount = matching_line.amount_with_gst
                    rec.pmsg_bank_account = matching_line.subsidy
                    rec.qty_solar_modules = matching_line.panel_nos
                else:
                    rec.total_payable_amount = 0
                    rec.pmsg_bank_account = 0
                    rec.qty_solar_modules = 0
