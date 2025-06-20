from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    crm_lead_match_id = fields.Many2one(
        'crm.lead',
        string="Matching CRM Lead",
        compute='_compute_crm_lead_match',
        store=True
    )

    @api.depends('consumer_name_mis')
    def _compute_crm_lead_match(self):
        for task in self:
            lead = self.env['crm.lead'].search([('partner_id.name', '=', task.consumer_name_mis)], limit=1)
            task.crm_lead_match_id = lead if lead else False

    def action_open_matching_crm_lead(self):
        self.ensure_one()
        if self.crm_lead_match_id:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'crm.lead',
                'res_id': self.crm_lead_match_id.id,
                'view_mode': 'form',
                'target': 'current',
            }
        return {'type': 'ir.actions.act_window_close'}


    def action_view_source_sale_orders_payments(self):
        self.ensure_one()
        if self.related_sale_order_id:
            return {
                'name': 'Sale Order',
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'view_mode': 'form',
                'res_id': self.related_sale_order_id.id,
                'target': 'current',
            }
        return {'type': 'ir.actions.act_window_close'}

    grid_type = fields.Selection([
        ('on_grid', 'On Grid'),
        ('hybrid', 'Hybrid'),
        ('off_grid', 'Off Grid'),
    ], string="Grid Type")

    estimated_value = fields.Char(string="Estimated Value")
    project_type = fields.Selection([
        ('kepl', 'Company'),
        ('dd', 'DD'),
        ('bd', 'BD'),
        ('pd', 'PD'),
    ], string="Project Type")

    pv_capacity_kw = fields.Float(string="PV Capacity (kW)")
    vendor_name_mis = fields.Char(string="Vendor Name MIS")

    mis_stage_id = fields.Many2one('project.task.type', string="2.0 MIS Stage")
    dispatch_stage_id = fields.Many2one('project.task.type', string="Dispatch Stage")

    project_ids = fields.Many2many('project.project', string="Project Name")

    consumer_name_mis = fields.Char(string="Consumer Name MIS")
    consumer_no_mis = fields.Char(string="Consumer No MIS")
    mobile_no_mis = fields.Char(string="Mobile No MIS")
    address_street1 = fields.Char(string="Address Street-1")
    address_street2 = fields.Char(string="Address Street-2")
    district = fields.Char(string="District")
    zip_code = fields.Char(string="Zip")
    consumer_state_mis = fields.Char(string="Consumer State MIS")
    application_date = fields.Date(string="Application Date")
    application_number = fields.Char(string="Application Number")
    discom_name = fields.Char(string="Discom Name")
    sanction_load = fields.Float(string="Sanction Load")
    existing_capacity = fields.Float(string="Existing Capacity")
    circle_name = fields.Char(string="Circle Name")
    division_name = fields.Char(string="Division Name")
    sub_division_name = fields.Char(string="Sub Division Name")
    registration_number = fields.Char(string="Registration Number")
    submitted_on = fields.Date(string="Submitted On")
    custom_modified_at = fields.Datetime(string="Modified At")
    feasibility_approved_date = fields.Date(string="Feasibility Approved Date")
    solar_installation_date = fields.Date(string="Solar Installation Date")
    project_inspection_date = fields.Date(string="Project Inspection Date")
    inspection_status = fields.Char(string="Inspection Status")
    project_commissioning_date = fields.Date(string="Project Commissioning Date")
    subsidy_redeem_date = fields.Date(string="Subsidy Redeem Date")
    subsidy_disbursed_date = fields.Date(string="Subsidy Disbursed Date")
    subsidy_verified_date = fields.Date(string="Subsidy Verified Date")
    application_pending_date = fields.Date(string="Application Pending Date")
    vendor_selection_date = fields.Date(string="Vendor Selection Date")
    upload_agreement_date = fields.Date(string="Upload Agreement Date")
    #
    related_sale_order_id = fields.Many2one('sale.order', string="Related Sale Order")
    ticket_numbers = fields.Char(string="Ticket Numbers")
    query = fields.Text(string="Query")
    liaisoning_comment = fields.Text(string="Comment by Liaisoning Team")

    pdc_file = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string="PDC File")

    pdc_agreement = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string="PDC Agreement")

    loan_taken = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string="Loan Taken")

    entry_date = fields.Date(string="Entry Date")
    deal_value = fields.Float(string="Deal Value")
    dcr_certificate_no = fields.Char(string="DCR Certificate No")

    is_installation = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string="Is Installation")

    is_commission = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string="Is Commission")

    consumer_r_total_invoiced = fields.Float(string="Consumer R Total Invoiced")
    consumer_r_due = fields.Float(string="Consumer R Due")
    consumer_r_invoice_no = fields.Char(string="Consumer R Invoice No")
    consumer_r_invoice_date = fields.Date(string="Consumer R Invoice Date")
    consumer_r_sale_date = fields.Date(string="Consumer R Sale Date")

    r_geo_latitude = fields.Float(string="R Geo Latitude", digits=(16, 7))
    r_geo_longitude = fields.Float(string="R Geo Longitude", digits=(16, 7))

    file_person = fields.Char(string="File Person")
    inside_sale_name = fields.Char(string="Inside Sale Name")
    dealer_name = fields.Char(string="Dealer Name")
    dealer_code = fields.Char(string="Dealer Code")
    installer_name = fields.Char(string="Installer Name")

    estimate_no = fields.Float(string="Estimate No")
    estimate_status = fields.Char(string="Estimate Status")
    meter_file = fields.Char(string="Meter File")
    stamp_300 = fields.Boolean(string="300 Stamp")
    stamp_50 = fields.Boolean(string="50 Stamp")
    agreement_discom = fields.Boolean(string="Agreement to DISCOM")
    meter_installation = fields.Boolean(string="Meter Installation")
    module_brand = fields.Char(string="Module Brand")
    module_wp = fields.Float(string="Module (Wp)")
    inverter_brand = fields.Char(string="Inverter Brand")
    installation_query = fields.Char(string="Installation Query")
    model_number = fields.Char(string="Model Number")
    inverter_number = fields.Char(string="Inverter Number")
    inverter_capacity = fields.Char(string="Inverter Capacity")

    consumer_aadharcard = fields.Binary(string="Consumer Aadharcard")
    consumer_electricity_bill = fields.Binary(string="Consumer Electricity Bill")
    consumer_pan = fields.Binary(string="Consumer Pan")
    consumer_cheque = fields.Binary(string="Consumer Cheque")
    consumer_taxbill = fields.Binary(string="Consumer Taxbill")
    other_docs_1 = fields.Binary(string="Other Docs-1")
    other_docs_2 = fields.Binary(string="Other Docs-2")
    application_letter = fields.Binary(string="Application Letter")
    feasibility_letter = fields.Binary(string="Feasibility Letter")
    estimate_paid_receipt = fields.Binary(string="Estimate Paid Receipt")
    consumer_bank_statement = fields.Binary(string="Consumer Bank Statement")
    model_agreement_pdf = fields.Binary(string="Model Agreement Pdf")
    ppa_agreement_300_stamp = fields.Binary(string="PPA Agreement (300 stamp)")

    aging_dsd = fields.Integer(string="Aging_DSD")
    aging_sid = fields.Integer(string="Aging_SID")
    aging_atd = fields.Integer(string="Aging_ATD")
    aging_scd = fields.Integer(string="Aging_SCD")
    aging_lmd = fields.Integer(string="Aging_LMD")

    subsidy_received_days = fields.Integer(string="Subsidy Received (Days)")
    custom_update = fields.Char(string="Update")
    accounts_team = fields.Char(string="Accounts Team")
    zone = fields.Char(string="Zone")
    application_aging = fields.Integer(string="Application Aging")
    vendor_selection = fields.Integer(string="Vendor Selection")
    upload_agreement = fields.Integer(string="Upload Agreement")
    installation = fields.Integer(string="Installation")
    project_inspection = fields.Integer(string="Project Inspection")
    project_commissioning = fields.Integer(string="Project Commissioning")
    subsidy_request = fields.Integer(string="Subsidy Request")
    subsidy_disbursal = fields.Integer(string="Subsidy Disbursal")

    c_inverter_number = fields.Char(string="C_Inverter Number")
    e_today = fields.Float(string="E-Today")


class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.model_create_multi
    def create(self, vals_list):
        projects = super(ProjectProject, self).create(vals_list)
        for project in projects:

            default_stages = [
                'Registration', 'Application', 'Feasibility', 'Vendor Selection',
                'Upload Agreement', 'Installation', 'Inspection',
                'Project Commissioning', 'Subsidy Request', 'Subsidy Disbursal'
            ]

            # Search for existing stages with the required names
            Stage = self.env['project.task.type']
            for stage_name in default_stages:
                # Case-insensitive name check
                stage = Stage.search([('name', '=ilike', stage_name)], limit=1)
                if not stage:
                    # Stage doesn't exist, create new and assign to current project
                    stage = Stage.create({
                        'name': stage_name,
                        'project_ids': [(4, project.id)]
                    })
                else:
                    # Stage exists, assign it to current project if not already assigned
                    if project.id not in stage.project_ids.ids:
                        stage.write({'project_ids': [(4, project.id)]})
        return projects
