from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def print_self_certificate(self):
        self.ensure_one()
        return self.env.ref('arclight_solar_report.self_certificate').report_action(self)

    def print_model_agreement(self):
        self.ensure_one()
        return self.env.ref('arclight_solar_report.model_agreement').report_action(self)

    def print_mgvcl_agreement(self):
        self.ensure_one()
        return self.env.ref('arclight_solar_report.mgvcl_agreement').report_action(self)

    def print_torrent_agreement(self):
        self.ensure_one()
        return self.env.ref('arclight_solar_report.torrent_agreement').report_action(self)