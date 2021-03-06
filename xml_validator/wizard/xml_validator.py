import base64
from lxml import etree

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class XMLValidator(models.TransientModel):
    _name = 'xml.validator'
    _description = 'XML Validator'

    xmlschema_doc = fields.Binary('XML Schema')
    xmlschema_doc_name = fields.Char('Filename XML Schema')
    xml_doc = fields.Binary('XML DOC')
    xml_doc_name = fields.Char('Filename XML DOC')

    def exist_files(self):
        if not self.xmlschema_doc:
            raise UserError(_('XML Schema: %s' % self.xmlschema_doc))
        else:
            if not self.xmlschema_doc_name.lower().endswith('.xsd'):
                raise UserError(_("XML Schema must be '.xsd'"))
        if not self.xml_doc:
            raise UserError(_('XML DOC: %s' % self.xml_doc))
        else:
            if not self.xml_doc_name.lower().endswith('.xml'):
                raise UserError(_("XML DOC must be '.xml'"))

    @api.multi
    def validate(self):
        self.exist_files()
        xmlschema_doc = etree.XML(base64.b64decode(self.xmlschema_doc))
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xml_doc = etree.XML(base64.b64decode(self.xml_doc))
        result = xmlschema.validate(xml_doc)
        raise UserError(result)
