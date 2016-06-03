function subscribe_to_new_answers() {
  var $info = $('#comments-cent-data');
  var centrifuge = new Centrifuge({
    url: $info.data('cent-url'),
    user: $info.data('cent-user').toString(),
    timestamp: $info.data('cent-ts').toString(),
    info: $info.data('cent-info'),
    token: $info.data('cent-token'),
    debug: true,
  });

  var channel = $info.data('cent-channel');
  console.log('subscribe on channel ' + channel);
  centrifuge.subscribe(channel, function(msg) {
    console.log('msg:' + msg);
    console.log('msg.data:' + msg.data);
    console.log('msg.data.text:' + msg.data.text);
    var row_html = '<li class="comment">' +
                    '<div class="comment-text">' + msg.data.text + '</div>' +
                    '<div class="comment-pub_date small">Дата создания: ' + msg.data.create_date + '</div>' +
                    '<div class="comment-change_date small">Дата последнего редактирования: ' + msg.data.change_date + '</div>' +
                    '</li>';
    $('.comment:first').before(row_html);
    console.log(row_html);
  });
  centrifuge.connect();
  return centrifuge;
}

var g_centrifuge = undefined;

$(document).ready(function() {
  g_centrifuge = subscribe_to_new_answers();
});