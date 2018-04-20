/**
 * Created by gua on 7/6/16 1:48:01
 */

// log
var log = console.log.bind(console)

// form
var formFromKeys = function (keys, prefix) {
    var form = {};
    for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var tagid = prefix + key;
        var value = $('#' + tagid).val();
        if (value.length < 1) {
            alert('字段不能为空');
            break;
        }
        form[key] = value;
    }
    return form;
};

// vip API
var vip = {
    data: {}
};

vip.ajax = function (url, method, form, success, error) {
    var request = {
        url: url,
        type: method,
        contentType: 'application/json',
        success: function (r) {
            // log('[vip success]', method, url, r);
            success(r);
        },
        error: function (err) {
            r = {
                success: false,
                data: err
            }
            // log('[vip error]', method, url, err, error);
            error(r);
        }
    };
    if (method.toLowerCase() === 'post') {
        log(method)
        var data = JSON.stringify(form);
        request.data = data;
    }
    $.ajax(request);
};

vip.get = function (url, response) {
    var method = 'get';
    var form = {}
    this.ajax(url, method, form, response, response);
};

vip.post = function (url, form, success, error) {
    var method = 'post';
    this.ajax(url, method, form, success, error);
};


vip.upload_file = function (url, key, fileobj, response) {
    // 要用一个 formdata 对象来装 file
    var formData = new FormData()
    formData.append(key, fileobj)
    var request = {
        url: url,
        method: 'post',
        // 下面这两个选项一定要加上
        contentType: false,
        processData: false,
        data: formData,
        success: function (r) {
            response(r)
        },
        error: function (err) {
            var r = {
                success: false,
                message: '上传文件失败',
                data: err
            };
            response(r)
        }
    }
    $.ajax(request)
}

vip.upload_files = function (url, key, files, response) {
    // 要用一个 formdata 对象来装 file
    var formData = new FormData()
    count = files.length
    if (count === 1) {
        formData.append(key, files[0])
    } else {
        for (var i = 0; i < count; i++) {
            var ikey = key + '_' + i
            formData.append(ikey, files[i])
        }
    }
    var request = {
        url: url,
        method: 'post',
        // 下面这两个选项一定要加上
        contentType: false,
        processData: false,
        data: formData,
        success: function (r) {
            response(r)
        },
        error: function (err) {
            var r = {
                success: false,
                message: '上传文件失败',
                data: err
            };
            response(r)
        }
    }
    $.ajax(request)
}


// API admin
vip.addBoard = function (form, success, error) {
    var url = '/admin/board/add';
    this.post(url, form, success, error);
};

vip.updatePermissions = function (form, success, error) {
    var url = '/admin/board/update';
    this.post(url, form, success, error);
};

// API normal
vip.register = function (form, success, error) {
    var url = '/register';
    this.post(url, form, success, error);
};

vip.login = function (form, success, error) {
    var url = '/login';
    this.post(url, form, success, error);
};

// board API
vip.board_all = function (response) {
    var url = '/api/boards';
    this.get(url, response);
};

vip.board = function (id, response) {
    var url = '/api/boards/' + id;
    this.get(url, response);
};

// topic API
vip.topicsInBoard = function (board_id, response) {
    var url = '/api/topics?board_id=' + board_id;
    this.get(url, response);
};

vip.topic = function (id, response) {
    var url = '/api/topics/' + id;
    this.get(url, response);
};

// 通知 api
vip.notificationRead = function (id, response) {
    var url = '/api/notification/read'
    id = Number(id)
    var form = {
        id: id,
    }
    this.post(url, form, response, response)
}

// model with cache
vip.model = function (type, id, response) {
    // var key = type
};


// --
// classroom api

// 获取科目下所有 lesson
vip.lessons = function(subjectId, response) {
    var url = '/api/subject/' + subjectId
    vip.get(url, response)
}

vip.discussAll = function (lessonId, response) {
    var url = '/api/discuss/all?lesson_id=' + lessonId
    this.get(url, response)
}


vip.taskAll = function (lessonId, response) {
    var url = '/api/task/all?lesson_id=' + lessonId
    this.get(url, response)
}

vip.myTasksWithHomework = function (lessonId, response) {
    var url = '/api/my_tasks_with_homework/' + lessonId
    this.get(url, response)
}

vip.discussWithReply = function (discussId, response) {
    var url = '/api/discuss_with_reply/' + discussId
    this.get(url, response)
}

vip.submitHomework = function (form, response) {
    var url = '/api/homework/submit'
    this.post(url, form, response)
}

vip.addDiscuss = function (lessonId, title, content, response) {
    var url = '/api/discuss/add'
    var form = {}
    form.lesson_id = lessonId
    form.content = content
    form.title = title
    this.post(url, form, response)
}

vip.addReply = function (DiscussId, content, response) {
    var url = '/api/reply/add'
    var form = {}
    form.discuss_id = DiscussId
    form.content = content
    this.post(url, form, response)
}

vip.enrollViolate = function (form, response) {
    var url = '/api/enroll/violate'
    this.post(url, form, response)
}

vip.homeworkDelay = function (form, response) {
    var url = '/api/homework/delay'
    this.post(url, form, response)
}