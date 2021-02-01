console.log('外部js加载成功');
console.log(blogData);
console.log(faderData);

$(function(){
  // 当页面元素加载完成后执行的代码
  // 使用faderData在页面中加载所有的轮播图
  // 图片路径通常随着项目位置发生变化 尽量不要直接写死图片
  // 采用地址+图片名的方式拼接路径

  var BASE_URL = '../static/images/';
  // var BASE_URL = 'http://127.0.0.1:8000/';
  // 遍历faderData 生成三个li标签 添加到页面元素.fader_controls之前
  
  
var html='';
$.each(faderData,function(i,o){
  html += `<li class="slide">
      <a href="#">
      <img src="${BASE_URL+o.img_url}">
      <span class="imginfo">
        ${o.img_info}
      </span>
      </a>
    </li>`
  })
  $('.fader_controls').before(html);

  // 调用 jquery.easyfader.min.js提供的轮播方法 实现图片切换效果
  $('.fader').easyFader();

// 先加载一部分博客内容
// 随着页面滚动 加载剩余内容

function add_blogs(data){
  var html='';
  $.each(data,function(i,o){
    html+=`<div class="blogs">
    <h3 class="blogtitle">
    <a href="#">
      ${o.blogtitle}
    </a>
  </h3>
  <!-- 博客图片 -->
  <div class="blogpic">
    <a href="#">
      <img src="${BASE_URL+o.blogpic}" alt="">
    </a>
  </div>
  <!-- 博客文字 -->
  <p class="blogtext">
    ${o.blogtext}
  </p>
  <!-- 用户列表 -->
  <!-- 14:15~14:35 -->
  <!-- 样式需求  li中的文字水平排列 调整距离 -->
  <!-- 文本颜色#748594 鼠标移入时 文字变黑 -->
  <!-- 背景图片 auicon.jpg  将背景图片添加给每一个li  分别调整每个li中背景图的位置 -->
  <ul>
    <li ${o.bloginfo.author}><a href="#">皮皮璐</a></li>
    <li ${o.bloginfo.lmname}><a href="#">学无止境</a></li>
    <li ${o.bloginfo.timer}><a href="#">2021-01-01</a></li>
    <li ${o.bloginfo.view}><a href="#">23456</a></li>
    <li ${o.bloginfo.like}><a href="#">9999</a></li>
  </ul>
  </div>`
  })
  $('.blogsbox').append(html);
}
// 随着页面滚动 每次滚动条快要到底时 加载剩余内容
add_blogs(blogData.slice(0,4));
$(document).scroll(function(){
  // 完整文档高度
  // 当前可视范围的高度
  var documentHeight = $(document).height();
  var windowHeight=$(document).height();
  var scrollTop = $(document).scrollTop();
  if(documentHeight-windowHeight-scrollTop<200)
  {
    //获取后面四条数据
    // 在页面上显示
    var size = $('.blogs').length;
    var data = blogData.slice(size,size+4);
    if(data.length>0){
      add_blogs(data)
    }
  }
})
})