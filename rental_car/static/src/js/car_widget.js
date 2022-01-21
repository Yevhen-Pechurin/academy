odoo.define('rental_car.car_widget', function (require) {
    'use strict';

    const {qweb} = require('web.core');

    const FieldChar = require('web.basic_fields').FieldChar;
    const fieldRegistry = require('web.field_registry');

    const CustomFieldChar = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
        }),
        init: function () {
            this._super.apply(this, arguments);
            // console.log('My Test Field - 222');
            this.data = [];
        },
        _onInput: function () {
            // console.log(this.$el.val());
            const self = this;
            const query = this.$el.val();
            this._rpc({
                model: 'res.partner',
                method: 'get_partner_list',
                args: [query],
            }).then(function (data) {
                self.$el.parent().fild('car_search_div').remove()
                if (data.partner_list.length > 0) {
                    const element = $(qweb.render('car_info.list_partner', {
                        list_partner: data.partner_list

                    }));
                    element.find('.car_search_ul').on('click', self.onClickList.bind(self))
                    self.$el.after(element)
                    }
                })
            },
        onClickList: function (e) {
            const self = this;
            const id = e.target.dataset.id
            if (id) {
                return;
            }
            this._rpc({
                model: 'res.partner',
                method: 'get_partner_info',
                args: [id],
            }).then(function (data) {
                const changes = {
                  phone: data[0].phone || '',
                  email: data[0].email || '',
                  name: data[0].name || '',
                }
                self.$el.val(data[0].name);
                self.trigger_up( 'field_changed',{
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: changes
                });
                self.$el.parent().find('.car_search_div').remove()
            })

        }
    });

    fieldRegistry.add('my_custom_field', CustomFieldChar);

    // return {CustomFieldChar, Widget}
})

