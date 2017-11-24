var pagetitle = new Vue ({
	el: '#pageTitle',
	data: {
		title: 'RitsuShare',
		subTitle: 'Share everything you like.'
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
