from odoo import models, fields, api


class ReportExample(models.Model):
    _name = "example.xlsx.wizard"
    _description = "Report Example"

    name = fields.Char()
    description = fields.Text()
    start_date = fields.Date()
    end_date = fields.Date()
    amount = fields.Float()
    active = fields.Boolean(default=True)

    @api.model
    def get_report_values(self, docids, data=None):
        docs = self.env["report.example"].browse(docids)
        return {
            "doc_ids": docids,
            "doc_model": "report.example",
            "docs": docs,
            "data": data,
        }
