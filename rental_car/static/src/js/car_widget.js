odoo.define('rental_car.car_widget', function (require) {
    'use strict';

    const Widget = require('web.Widget');

    const CarWidget = Widget.extend({
        init: function () {
            console.log('Test01 test02 test03');
            this.data = [];
        },

        // start: function () {
        //     this._super(this, arguments);
        // },
    });

    return {CarWidget}
})
