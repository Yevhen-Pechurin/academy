odoo.define('rental.services', function (require) {
    "use strict";

    const getData = async (self, query) => {
        await self.env.services.rpc({
            model: 'rental.car',
            method: 'get_model',
            args: [query],
        })
    }
    return {getData}
})