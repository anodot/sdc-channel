# todo state deprecated?
global sdc, state

try:
    sdc.importLock()
    from string import Template
    import json
finally:
    sdc.importUnlock()


for record in sdc.records:
    ticket = Template(state['TEMPLATE']).safe_substitute(record.value['variables'])
    ticket = json.loads(ticket, strict=False)

    new_record = sdc.createRecord('Anodot alert')
    new_record.value = ticket
    try:
        sdc.log.info("Output record: " + str(new_record.value))
        sdc.output.write(new_record)
    except Exception as e:
        sdc.error.write(new_record, str(e))
