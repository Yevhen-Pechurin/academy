odoo.define('rental.body', function (require) {
    'use strict';

    const Widget = require('rental.engine');

    const Body = Widget.extend({
        init: function (parent, capacity, weight) {
            this._super(parent, capacity);
            this.weight = weight;
            this.speed = (this.speed_coefficient * this.weight) / 25
        },

    });
        return Body;
})