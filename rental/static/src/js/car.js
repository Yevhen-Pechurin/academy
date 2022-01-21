odoo.define('rental.car', function (require) {
    'use strict';
    const FieldChar = require('web.basic_fields').FieldChar;
    const fieldRegistry = require('web.field_registry');
    const core = require('web.core')
    const Qweb = core.qweb

    const CustomFieldChar = FieldChar.extend({
        init: function () {
            this._super.apply(this, arguments); // забирает все наши extend
            console.log('TEST');
        },
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput'
        }),
        _onInput: async function () {
            const self = this;

            this._rpc({
                model: 'rental.car',
                method: 'get_car_list',
                args: [this.$el.val()],
            }).then(function (data) {
                self.$el.parent().find('.zoom_search_div').remove();
                if (data.car_list.length > 0) {
                    const element = $(Qweb.render('rental.car_list', {
                        car_list: data.car_list
                    }));
                    element.find('.car_search_list').on('click', self.onClickList.bind(self))
                    self.$el.after(element);
                }
            })
        },
        onClickList: function (e) {
            const self = this
            const id = e.target.dataset.id
            if (!id) {
                return
            }
            this._rpc({
                model: 'rental.car',
                method: 'get_car_info',
                args: [id]
            }).then(function (data) {

                const changes = {
                    year: data[0].year || '',
                    odometer: data[0].odometer || '',
                    model: data[0].model
                }

                self.$el.val(data[0].model)
                self.trigger_up('field.changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: changes
                });
                self.$el._parent().find('zoom_search_div').remove()
        })
    }})


    fieldRegistry.add('list_field', CustomFieldChar);
})
