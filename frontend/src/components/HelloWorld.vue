<template>
  <div class="hello">
    <div class="col-md-18">
      <div class="info_list info-index-list">
      <ul>
                    <li><span class="info_time">2020-07-24</span><a href="?mod=info&act=view&id=4062" title="Is it a bird, a plane? Not superman, but a flapping wing drone">Is it a bird, a plane? Not superman, but a flapping wing drone</a></li>
                    <li><span class="info_time">2020-07-24</span><a href="?mod=info&act=view&id=4061" title="3D hand-sensing wristband signals future of wearable tech">3D hand-sensing wristband signals future of wearable tech</a></li>
                    <li><span class="info_time">2020-07-24</span><a href="?mod=info&act=view&id=4060" title="Powerful human-like hands create safer human-robotics interactions">Powerful human-like hands create safer human-robotics interactions</a></li>
                    <li><span class="info_time">2020-07-16</span><a href="?mod=info&act=view&id=4059" title="Researchers 3D print a working heart pump with real human cells Discovery could open new doors for heart research">Researchers 3D print a working heart pump with real human cells Discovery cou…</a></li>
                    <li><span class="info_time">2020-07-13</span><a href="?mod=info&act=view&id=4058" title="Like humans, beluga whales form social networks beyond family ties Study first to uncover the role kinship plays in complex groupings and relationships of beluga whales spanning 10 locations across the Arctic">Like humans, beluga whales form social networks beyond family ties Study firs…</a></li>
                    <li><span class="info_time">2020-07-09</span><a href="?mod=info&act=view&id=4057" title="Animals who try to sound &#39;bigger&#39; are good at learning sounds">Animals who try to sound &#39;bigger&#39; are good at learning sounds</a></li>
                    <li><span class="info_time">2020-07-04</span><a href="?mod=info&act=view&id=4053" title="Jellyfish-inspired soft robots can outswim their natural counterparts">Jellyfish-inspired soft robots can outswim their natural counterparts</a></li>
                    </ul>
      </div>
      </div>
  </div>
</template>

<script>
export default {
    name: "HelloWorld",
    data() {
        return {
            msg: ""
        };
    },


  created () {//增加了这个函数,其它没变
    this.axios.get('/myapp/test').then(response => {
      this.msg = response.data;
      console.log(response.data)
    })
  }



};
</script>

