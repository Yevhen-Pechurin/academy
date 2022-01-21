// odoo.define('rental_car.role', function (require) {
//     'use strict';
//
//     const Class = require('web.Class');
//     console.log('Консоль, Заработало)))))')
//     const Role = Class.extend({
//         init: function () {
//             this.position = 0;
//             // this.fuel = 100
//         },
//         turn_left: function () {
//             // this.fuel = this.fuel - 1;
//             this.position = this.position - 1;
//             console.log('turn_left', this.position);
//         },
//         turn_right: function () {
//          // this.fuel = this.fuel - 1;
//             this.position = this.position + 1;
//             console.log('turn_right', this.position);
//         },
//         beep: function (){
//             console.log('Консоль, Beep)))))');
//         },
//     });
//
//
//     const role = new Role();
//     role.turn_left()
//     role.turn_left()
//     role.turn_left()
//     role.turn_right()
//     role.beep()
//     console.log('position = ', role.position)
// })