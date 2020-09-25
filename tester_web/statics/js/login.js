/**
 * Created by xiaon on 2020/9/10.
 */
/**
 * Created by xiaon on 2020/7/28.
 */

var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'

  }
});

var app2 = new Vue({
  el: '#app2',
  data: {
    message: '页面加载于' + new Date().toLocaleString()
  }
})
;

var app3 = new Vue({
  el: '#app3',
  data: {
    seen: false
  }
});

var app4 = new Vue({
  el: '#app4',
  data: {
    todos: [
      { text: '学习vue' },
      { text: 'who am I' },
      { text: '开整' }
    ]
  }
});

var app5 = new Vue({
  el: '#app5',
  data: {
    message1: 'Hello Vue!'
  },
  methods: {
    reverseMessage: function () {
      this.message1 = this.message1.split('').reverse().join('')
    }
  }
});

var app6 = new Vue({
  el: '#app6',
  data: {
    message2: 'interesting vue'
  }
});

Vue.component('todo-item', {
  // todo-item 组件现在接受一个
  // "prop"，类似于一个自定义 attribute。
  // 这个 prop 名为 todo。
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
});

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: '蔬菜' },
      { id: 1, text: '奶酪' },
      { id: 2, text: '随便其它什么人吃的东西' }
    ]
  }
});
// var app7 = new Vue({
//   el: '#app7',
//   data: {
//     groceryList: [
//       { id: 0, text: '蔬菜' },
//       { id: 1, text: '奶酪' },
//       { id: 2, text: '随便其它什么人吃的东西' }
//     ]
//   }
// });




