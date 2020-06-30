import xml.dom.minidom


def name(doctype: xml.dom.minidom.DocumentType):
    return doctype.name


def publicId(doctype: xml.dom.minidom.DocumentType):
    return doctype.publicId


def systemId(doctype: xml.dom.minidom.DocumentType):
    return doctype.systemId
