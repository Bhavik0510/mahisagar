from odoo import models, api
from datetime import date

class ReportSaleOrderCustom(models.AbstractModel):
    _name = 'report.sale_order_pdf_button.custom_sale_order_report_template'
    _description = 'Custom Sale Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'report_date': date.today().strftime('%d-%m-%Y'),
            'docs': docs,
        }


class ReportSaleOrderCustomProposal(models.AbstractModel):
    _name = 'report.sale_order_pdf_button.custom_sale_order_proposal_report_template'
    _description = 'Custom Sale Order Proposal Report'

    @api.model
    def _get_report_values_proposal(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'report_date': date.today().strftime('%d-%m-%Y'),
            'docs': docs,
        }
