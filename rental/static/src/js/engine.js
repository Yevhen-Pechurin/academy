odoo.define('rental.engine', function (require) {
    'use strict';

    const Widget = require('web.Widget');

    const Engine = Widget.extend({
        init: function (parent, capacity) {
            this._super(parent);
            this.capacity = capacity;
            this.speed_coefficient = capacity/250
        },

    });
        return Engine;
})