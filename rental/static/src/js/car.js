odoo.define('rental.car', function (require) {
    'use strict';
    const Widget = require('web.Widget');
    const Body = {
        damage: function (dmg) {
            if (this.durability - dmg > 0) {
                this.durability -= dmg;
            } else {
                console.log('Car was broken')
            }
        },
        painting: function (color) {
            this.color = color;
        }
    };
    const Motor = {

        new_motor: function (new_model, max_speed) {
            this.model = new_model;
            this.max_speed = max_speed;

        }
    };
    const Car = Widget.extend(Body, Motor, {
        template: 'rental.actions',
        events: {
            'click .drive': 'drive',
            'click .speed_up': 'speed_up',
            'click .check_max_speed': 'check_max_speed',

        },
        init: function (parent) {
            this._super(parent);
            this.model = 'default_model'
            this.max_speed = 160;
            this.speed = 0;
            this.durability = 100;
            this.color = 'red';
        },
        drive: function () {
            console.log('Driving...');
            this.speed = 80;
        },
        speed_up: function () {
            if (this.speed != 0 & this.speed<this.max_speed) {
                this.speed += 20;
                console.log(this.speed);
            } else {
                console.log('Problem')
            }
        },
        check_max_speed:function (){
            console.log(this.max_speed);
        }

    });
    var car1 = new Car(this)
    require('web.dom_ready')


    car1.appendTo("body");
})