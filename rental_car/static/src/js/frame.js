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

})