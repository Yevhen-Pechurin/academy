odoo.define('rental.car', function (require) {
    'use strict';

    const Widget = require('rental.body');

    const Car = Widget.extend({
        template: 'rental.car',
        events: {
            'click .forward_btn': '_onClick_forward',
            'click .backward_btn': '_onClick_backward',
        },
        init: function (parent, capacity, weight, first_pos) {
            this._super(parent, capacity, weight);
            this.pos = first_pos;
        },
        _onClick_forward: function () {
            this.pos += this.speed;
            this.$('.val').text(this.pos);
        },
        _onClick_backward: function () {
            this.pos -= this.speed;
            this.$('.val').text(this.pos);
        },
    });
    require('web.dom_ready')
    var car = new Car(this, 500, 1000, 25);
    car.appendTo("body");
})