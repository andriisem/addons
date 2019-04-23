from odoo import models, fields, api

try:
    from lxml import etree
except ImportError:
    raise ImportError(
        'Please install lxml on your system. (sudo pip3 install lxml)')


class XMLValidator(models.TransientModel):
    _name = 'xml.validator'
    _description = 'XML Validator'

    xmlschema_doc = fields.Binary('XML Schema')
    xmlschema_doc_name = fields.Char(size=256, readonly=True)
    xml_doc = fields.Binary('XML DOC')
    xml_doc_name = fields.Char(size=256, readonly=True)

    @api.multi
    def validate(self):
        pass

