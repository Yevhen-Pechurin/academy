odoo.define('rental_car.frame', function (require) {
    'use strict';

    const Class = require('web.Class');

    const Frame = Class.extend({
        init: function () {
            this.x = 1;
            this.y = 3;
        },
    });

    return {Frame};
})