<template>
<div class="hello">

<div class="aside">
        <h2 class="aside-title">系统概要</h2>
        <img  class="asideimage" src="../../static/pictures/11.jpg" alt=""><br>
        <img  class="asideimage" src="../../static/pictures/12.jpg" alt=""><br>
        <img  class="asideimage"src="../../static/pictures/13.jpg" alt=""><br>
        <img  class="asideimage" src="../../static/pictures/14.jpg" alt=""><br>
    
</div>



<div class="title">
   <h1 class="title-text">  生物群体行为</h1>
   <img  class="title-img" src="../../static/pictures/6.jpg" alt="">
   <div class="demo-input-suffix">
    <el-input placeholder="请输入内容"  prefix-icon="el-icon-search"  v-model="input2"> </el-input>
   </div>
   <nav class="navbar-default">
    <div class="navbar" > 
     <ul >
       <li class=link><a calss="tlink" href="https://www.baidu.com/">首页</a></li>
       <li class=link><a calss="tlink" href="https://www.baidu.com/">搜索</a></li>
       <li class=link><a calss="tlink" href="https://www.baidu.com/">APIs</a></li>
       <li class=link><a calss="tlink" href="https://www.baidu.com/">论文</a></li>
       <li class=link><a calss="tlink" href="https://www.baidu.com/">关于</a></li>
     </ul>
 </div>
</nav>
</div>

<div class="main-img">
    <el-carousel indicator-position>
        <el-carousel-item v-for="item in imagesbox" :key="item.pk">
            <a v-bind:href="item.link"><img :src="item.path" class="image" width="1100px" height="300px"> </a>
        </el-carousel-item >
    </el-carousel>
</div>

<div class="main-introduce">
    <div class="main-introduce-title1"><h2 class="main-introduce-title">生物行为介绍</h2><el-divider></el-divider></div>
    <p  class="main-introduce-text">
        猫，喜欢食肉，善于夜间活动，犬齿十分达，爪子也很锐利，
        善于捕捉小物，在野处觅食的猫有还会捕捉青蛙，也
        常吃粮食类的熟食。喜欢清洁卫生。听觉也特别灵，日常生活中
        凭听觉来注意察觉周围的动静，探知老鼠的活动地点。猫捕鼠时注意
        力集中，严阵以待。家庭中的小猫在一定程度上同样保持着野猫昼伏夜出的习性。</p> 
</div>

<div class="main-paper">
    <div class="papertitle1"><br><h2 class="papertitle">最新论文摘要</h2><br><el-divider></el-divider></div>
    <el-table
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
    <el-table-column
      prop="name"
      label="标题"
      width="480">
      <template slot-scope="scope">
        <a v-bind:href="scope.row.link" >{{scope.row.name}}</a>
    </template>
    </el-table-column>
    <el-table-column
      prop="date"
      label="日期"
      width="180">
      
    </el-table-column>
    </el-table>

</div>

<div class="footer">
    <div class="title-foot1"><h2 class="title-foot">帮助 </h2><br><br><el-divider></el-divider></div>
    <p class="foot-help">狮子是森林之王 老虎是草原之王 </p>
</div>

</div>

</template>

<script>
export default {
    name: "Home",
    methods: {
      tableRowClassName({row, rowIndex}) {
        if (rowIndex === 1) {
          return 'warning-row';
        } else if (rowIndex === 3) {
          return 'success-row';
        }
        return '';
      }
    },
    data() {
            
        return {
            imagesbox:[
            {pk:0,path:"",link:""},   
            {pk:1,path:"",link:""},
            {pk:3,path:"",link:""},
            {pk:4,path:"",link:""},],
            msg: "",
            input1: '',
             tableData: [{
             date: '',
             name: '',
             link: 'www.baidu.com'        
              }, {
            date: '2016-05-04',
            name: '王小虎',
            link: 'www.4399.com'   
            }, {
            date: '2016-05-01',
            name: '王小虎',
            link:'',
            }, {
            date: '2016-05-03',
            name: '王小虎',
            link:'',
            }]
      
           };
    },


  created () {
    this.axios.get('/myapp/est').then(response => {
     
       console.log(response.data)
        var ddd = JSON.parse(response.data);
        this.tableData[0].name=ddd[0].title;
        this.tableData[1].name=ddd[1].title;
        this.tableData[2].name=ddd[2].title;
        this.tableData[3].name=ddd[3].title;
        this.tableData[0].date=ddd[0].publishDate;
        this.tableData[1].date=ddd[1].publishDate;
        this.tableData[2].date=ddd[2].publishDate;
        this.tableData[3].date=ddd[3].publishDate;
        this.tableData[0].link=ddd[0].paperPath;
        this.tableData[1].link=ddd[1].paperPath;
        this.tableData[2].link=ddd[2].paperPath;
        this.tableData[3].link=ddd[3].paperPath;
    })
    this.axios.get('/myapp/test1').then(response => {
       this.msg = response.data;
       console.log(response.data)
        var ddd = JSON.parse(response.data);
        this.imagesbox[0].pk=ddd[0].id;
        this.imagesbox[1].pk=ddd[1].id;
        this.imagesbox[2].pk=ddd[2].id;
        this.imagesbox[3].pk=ddd[3].id;
        this.imagesbox[0].path=ddd[0].path;
        this.imagesbox[1].path=ddd[1].path;
        this.imagesbox[2].path=ddd[2].path;
        this.imagesbox[3].path=ddd[3].path;
        this.imagesbox[0].link=ddd[0].link;
        this.imagesbox[1].link=ddd[1].link;
        this.imagesbox[2].link=ddd[2].link;
        this.imagesbox[3].link=ddd[3].link;
       
    })
 
  }



};
</script>

<style type="text/css">

    .el-table .warning-row {
         background: oldlace;
    }

   .el-table .success-row {
        background: #f0f9eb;
   }
    .el-input{
        width: 300px;
        position: absolute;
        left:750px;
        top:30px;
    }
    .title-text{
        font-weight: bold;
        font-size: 50px;
        font-family: kaiti;
        color: rgb(0, 0, 0);
        position: absolute;
        left:125px;
        top:30px;
    }
    .title-img{
        height: 100px;
        position: absolute;
        left:10px;
       
    }
   
    .title{                                      
        background-image: url("../../static/pictures/5.jpg");
        width: 1100px;
        height:100px;
        position: absolute;
        left: 225px;
        top:0px;
       
    }

    .navbar{
        width: 1100px;
        height:50px;
        position: relative;
        right:0px;
        top:100px;
        background-color: rgb(17, 114, 224);
     }
    div.navbar li.link a{
        font-family:songti;
        position:relative;
        left:0px;
        top:-20px;
        display:inline;
        font-weight:bold;
        font-size:20px;
        color:rgb(255, 250, 250);
        display: inline;
        margin: 30px;
        float: left;
    }
   
    .main-img{
        background-color: rgb(46, 9, 104);
        width: 1100px;
        height:300px;
        position: absolute;
        left: 225px;
        top:150px;
        margin: 0px;
        padding: 0px;
      
    }
    .aside{
        background-image: url("../../static/pictures/5.jpg");
        width: 300px;
        height:700px;
        position:absolute;
        left: 225px;
        top:450px;
        margin: 0px;
        padding: 0px;
        display: flex;
        flex-flow: column;
    }
    .asideimage{
        height: 125px;
        width: 125px;
        position: relative;
        top:100px;
        left:90px;
       
    }
    .aside-title{
        font-weight: bold;
        font-size: 30px;
        font-family: songti;
        position: absolute;
        top:10px;
        left:90px;
        color:rgb(65, 65, 161);
    }
    .main-introduce{
        background-color:white;
        width: 775px;
        height:280px;
        position:absolute;
        left: 550px;
        top:450px;
        margin: 0px;
        padding: 0px;
    }
    .main-introduce-title1{
        background-color: rgb(17, 114, 224);
    }
    .main-introduce-title{
      
        position: relative;
        right:250px ;
        top:10px;
        font-size:30px;
        font-family: songti;
        color:rgb(236, 236, 243);
        font-weight: bold;
       
        
    }
    .main-introduce-text{
        text-indent: 1cm;
        text-align: left;
        font-family: songti;
    }
    .main-paper{
        background-color: rgb(255, 255, 255);
        width: 775px;
        height:400px;
        position:absolute;
        left: 550px;
        top:750px;
        margin: 0px;
        padding: 0px;
     }
     .papertitle1{
         background-color: rgb(17, 114, 224);
     }
     .papertitle{
        font-weight: bold;
        font-size: 30px;
        font-family: songti;
        position: absolute;
        top:10px;
        left:50px;
        color:rgb(253, 253, 255);
       
     }
    .footer{
        background-color: rgb(255, 254, 254);
        width: 1100px;
        height:200px;
        position:absolute;
        left: 225px;
        top:1170px;
        margin: 0px;
        padding: 0px;
    }
    .title-foot1{
        background-color:rgb(17, 114, 224);
    }
    .title-foot{
        font-weight: bold;
        font-size: 30px;
        font-family: songti;
        position: absolute;
        top:10px;
        left:20px;
        color:rgb(238, 238, 240);
    }
    .foot-help{
        text-indent: 1cm;
        text-align: left;
        font-family: songti;
    }
  
</style>