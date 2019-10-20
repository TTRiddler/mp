$(document).ready(function(){
    $('#FeedBackForm button').click(function(e) { 
        e.preventDefault();

        csrf_token = $('#FeedBackForm [name="csrfmiddlewaretoken"]').val();
        recaptcha = $('#FeedBackForm [name="g-recaptcha-response"]').val();
        name = $('#FeedBackForm [name="name"]').val();
        email = $('#FeedBackForm [name="email"]').val();
        text = $('#FeedBackForm [name="text"]').val();
        
		data = {
            "csrfmiddlewaretoken": csrf_token,
            'g-recaptcha-response': recaptcha,
            email: email,
            name: name,
            text: text,
        }

		$.ajax({
			type: "POST",
			url: $('#FeedBackForm').attr('action'),
			data: data,
			success: function(data) {
                $('#FeedBackForm').removeClass('needs-validation');
                $('#FeedBackForm').addClass('was-validated');
                switch(data.sended) {
                    case 0: 
                        $('.modal .email-error').removeClass('d-none');
                        break;
                    case 1: 
                        $('.modal .modal-success').removeClass('d-none');
                        $('.modal .modal-success').addClass('d-flex');
                        break;
                  }
            }
		});
    });

    $('#more_news button').click(function(e) { 
        e.preventDefault();
        
        var link = $(this);
        var page = link.data('page');
        
        csrf_token = $('#more_news [name="csrfmiddlewaretoken"]').val();
        
		data = {
            'page': page,
            "csrfmiddlewaretoken": csrf_token,
        }

		$.ajax({
			type: "POST",
			url: $('#more_news').attr('action'),
			data: data,
			success: function(data) {
                if (data.has_next) {
                    link.data('page', page+1);
                } else {
                  link.hide();
                }
                
                $('#news').append(data.news_html);
            }
		});
    });
});