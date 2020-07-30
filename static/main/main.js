function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  
  function likePost(postId) {
    return fetch('/post/' + postId + '/like/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }).then(() => {
      document.location.reload(true)
    })
  }
  
  function commentPost(postId, comment) {
    const formData = new FormData()
    formData.append('content', comment)
    return fetch('/post/' + postId + '/comment/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: formData,
    }).then(() => {
      document.location.reload(true)
    })
  }

  function sendRequest(recieverId) {
    return fetch('/request/' + recieverId + '/add/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }).then(() => {
      document.location.reload(true)
    })
  }
  
  function addfriend(recieverId) {
    return fetch('/add/' + recieverId + '/friend/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }).then(() => {
      document.location.reload(true)
    })
  }

  function cancel(recieverId) {
    return fetch('/cancel/' + recieverId + '/friend/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }).then(() => {
      document.location.reload(true)
    })
  }