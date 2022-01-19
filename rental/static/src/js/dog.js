odoo.define('rental.dog', function (require) {
    'use strict';
    const Animal = require('rental.animal');

    const Dog = Animal.extend({
        move: function () {
            this.bark();
            this._super.apply(this, arguments);
        },
        bark: function () {
            console.log('woof');
        },
    });
    const dog = new Dog();
    dog.move()
})






// odoo.define('rental.dog', function (require) {
//     'use strict';
//     const Animal = require('rental.animal');
//     const DanceMixin = {
//         dance: function () {
//             console.log('dancing...');
//         },
//     };
//     const Dog = Animal.extend(DanceMixin, {
//         move: function () {
//             this._super.apply(this, arguments);
//             this.bark();
//         },
//         bark: function () {
//             console.log('woof');
//         },
//     });
//
//     Animal.include({
//         init: function () {
//             this._super.apply(this, arguments);
//             console.log('init', this.x, this.hunger);
//         },
//         move: function () {
//             this.x = this.x + 1;
//             this.hunger = this.hunger + 1;
//         },
//     })
//     const animal = new Animal();
//     animal.move();
// })