// odoo.define('rental.model_widget', function (require) {
//     'use strict';
//
//     const {qweb} = require('web.core');
//
//     const FieldChar = require('web.basic_fields').FieldChar;
//
//     const CustomFieldChar = FieldChar.extend({
//         events: _.extend({}, FieldChar.prototype.events, {
//             'input': '_onInput',
//         }),
//         init: function () {
//             this._super(...arguments);
//         },
//         _onInput: function () {
//             const self = this;
//             const query = this.$el.val()
//             this._rpc({
//                 model: 'rental.car.info',
//                 method: 'get_car_list',
//                 args: [query],
//             }).then(function (data) {
//                 debugger
//                 self.$el.parent().find('.rental_search_div').remove();
//                 if (data.car_list.length > 0) {
//                     const element = $(qweb.render('rental.list_car', {
//                         list_car: data.car_list
//                     }));
//                     element.find('.rental_search_ul').on('click', self.onClickList.bind(self))
//                     self.$el.after(element);
//                 }
//             })
//         },
//         onClickList: function (e) {
//             const self = this;
//             const id = e.target.dataset.id
//             if (!id) {
//                 return;
//             }
//             this._rpc({
//                 model: 'rental.car.info',
//                 method: 'get_car_info',
//                 args: [id],
//             }).then(function (data) {
//
//                 const changes = {
//                     name: data[0].name || '',
//                     model: data[0].model || '',
//                     country: data[0].country || '',
//                 }
//                 self.$el.val(data[0].name);
//                 self.trigger_up('field_changed', {
//                     dataPointID: self.dataPointID,
//                     operation: 'UPDATE',
//                     changes: changes
//                 });
//                 self.$el.car().find('.rental_search_div').remove()
//             })
//
//         }
//     });
//
//     const fieldRegistry = require('web.field_registry');
//
//     fieldRegistry.add('my_custom_field', CustomFieldChar);
//
// });





// <t t-name="rental.list_car">
//     <div className="rental_search_div">
//         <ul className="rental_search_ul list-unstyled">
//             <li t-foreach="list_car" t-as="car" className="rental_search_li">
//                 <p className="list_car_span" t-esc="car['name']" t-att-data-id="car['id']"/>


//     const Widget = require('web.Widget');
//
//     var FieldChar = require('web.basic_fields').FieldChar;
//     var FieldRegistry = require('web.field_registry');
//
//     var CustomFieldChar = FieldChar.extend({
//         className: 'o_field_partner_rental',
//
//         // xmlDependencies: ['/rental/static/src/xml/model_widget.xml'],
//         // template: 'rental.rental_template',
//
//         events: _.extend({}, FieldChar.prototype.events, {
//             'input': '_onInput',
//         }),
//         init: function () {
//             this._super.apply(this, arguments);
//             console.log('TEST WORK');
//             this.data = [];
//         },
//
//         _onInput: function () {
//             console.log(this.$el.val());
//             // this._rpc({
//             //     model: 'res.partner',
//             //     method: 'get_country',
//             //     args: ['1', "1"],
//             // });
//         }
//
//     });
//
//     FieldRegistry.add('my_custom_field', CustomFieldChar);
// })


