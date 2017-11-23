var pagetitle = new Vue ({
	el: '#pageTitle',
	data: {
		title: 'RitsuCoder',
		subTitle: 'Build your personal page with one-click!'
	}
})

var filelist = new Vue({
  el: '#fileTable',
  data: {
    files: null
  },
  mounted () {
    this.files = filelistjs;
  }
})