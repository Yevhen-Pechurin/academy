odoo.define('zoom_info.zoom_info_query', function (require) {
    'use strict';

    const findCompanyId = (self, query) => {
        return self._rpc({
            model: 'zoom.info',
            method: 'find_company_id',
            args: [query],
        })
    }

    const findCompanyInfo = (self, companyId) => {
        return self._rpc({
            model: 'zoom.info',
            method: 'find_company_info',
            args: [companyId],
        })
    }

    const getCountryState = (self, country, state) => {
        return self._rpc({
            model: 'res.partner',
            method: 'get_country',
            args: [],
            kwargs: {
                country_name: country,
                state_name: state,
            },
        })
    }

    const findContactByName = (self, name, companyId) => {
        return self._rpc({
            model: 'zoom.info',
            method: 'find_contact_by_name',
            args: [name, companyId],
        })
    }

    const findContactByPosition = (self, jobTitle, companyId) => {
        return self._rpc({
            model: 'zoom.info',
            method: 'find_contact_by_position',
            args: [jobTitle, companyId]
        })
    }

    const findContactInfo = (self, personId) => {
        return self._rpc({
            model: 'zoom.info',
            method: 'find_contact_info',
            args: [personId],
        })
    }

    return {
        findCompanyId,
        findCompanyInfo,
        getCountryState,
        findContactByName,
        findContactByPosition,
        findContactInfo
    }
})