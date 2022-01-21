odoo.define('rental_car.car', function (require) {
    'use strict';

    const Widget = require('web.Widget');

    const Car = Widget.extend({
        xmlDependencies: ['/rental_car/static/src/xml/car.xml'],
        template: 'rental_car.car',
        events: {
            'click .add_car_btn': '_add',
            'click .remove_car_btn': '_remove',
            'click .multiply_car_btn': '_multiply',
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
            this.count = this.count - 2;
            this.$('.val').text(this.count);
            console.log('My Test Field - 11');
        },
        _multiply: function () {
            this.count = this.count * 2;
            this.$('.val').text(this.count);
        }
    });

    require('web.dom_ready')
    const car = new Car(this, 10);
// Render and insert into DOM
    car.appendTo("body");

    return {Car};
})