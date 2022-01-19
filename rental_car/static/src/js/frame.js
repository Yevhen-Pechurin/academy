odoo.define('rental_car.frame', function (require) {
    'use strict';

    const Class = require('web.Class');

    const Frame = Class.extend({
        init: function () {
            this.x = 0;
            this.hunger = 0;
        },
        move: function () {
            this.x = this.x + 1;
            this.hunger = this.hunger + 1;
            console.log('move', this.x, this.hunger);
        },
        eat: function () {
            this.hunger = 0;
        },
    });

    const Widget = require('web.Widget');

    const Counter = Widget.extend({
        template: 'rental_car.car',
        events: {
            'click .add_car_btn': '_add',
            'click .remove_car_btn': '_remove',
            'multiply_car_btn': '_multiply',
        },
        init: function (parent, value) {
            this._super(parent);
            this.count = value;
        },
        _add: function () {
            this.count++;
            this.$('.val').text(this.count);
        },
        _remove: function () {
            setInterval(() => {
                this.count++;
                this.$('.val').text(this.count);
            }, 100)
        },
        _multiply: function () {
            setInterval(() => {
                this.count++;
                this.$('.val').text(this.count);
            }, 100)
        }
    });

    require('web.dom_ready')
    var counter = new Counter(this, 4);
// Render and insert into DOM
    counter.appendTo("body");

    // return Animal;

    return {Frame, Counter};
})