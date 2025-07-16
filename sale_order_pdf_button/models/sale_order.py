from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def print_custom_report(self):
        return self.env.ref('sale_order_pdf_button.custom_sale_order_report').report_action(self)

    x_custom_logo = fields.Binary(string="Custom Logo")
