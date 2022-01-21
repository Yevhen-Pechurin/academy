odoo.define('rental.car', function (require) {
    'use strict';
    const core = require('web.core');
    const qweb = core.qweb;

    const FieldChar = require('web.basic_fields').FieldChar;

    const fieldRegistry = require('web.field_registry');
    const CustomFieldChar = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
        }),
        init: function () {
            this._super.apply(this, arguments);
        },
        _onInput: function () {
            const self = this;
            const query = this.$el.val()
            this._rpc({
                model: 'rental.car',
                method: 'get_model',
                args: [query],
            }).then((data) => {
                self.$el.parent().find('.rental_search_div').remove();
                if (data.model_list.length > 0) {
                    const element = $(qweb.render('rental.list_car', {
                        list_partner: data.model_list
                    }));
                    element.find('.rental_search_ul').on('click', self.onClickList.bind(self))
                    self.$el.after(element);

                }
            })
        },
        onClickList: function (e) {
            const self = this;
            const id = e.target.dataset.id
            if (!id) {
                return;
            }
            this._rpc({
                model: 'rental.car',
                method: 'get_model_info',
                args: [id],
            }).then(function (data) {

                const changes = {
                    name: data[0].name || '',
                    number: data[0].number || '',
                }
                self.$el.val(data[0].name);
                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: changes
                });
                self.$el.parent().find('.rental_search_div').remove()
            })

        }
    })

    fieldRegistry.add('my-custom-field', CustomFieldChar);
});
