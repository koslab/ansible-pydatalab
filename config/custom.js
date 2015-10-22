require.config({
  paths: {
      d3: '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min',
      nvd3: '//cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.1/nv.d3.min',
      dimplejs: '//cdnjs.cloudflare.com/ajax/libs/dimple/2.1.6/dimple.latest.min',
      crossfilter: '//cdnjs.cloudflare.com/ajax/libs/crossfilter/1.3.12/crossfilter.min',
      dcjs: '//cdnjs.cloudflare.com/ajax/libs/dc/1.7.4/dc.min'

  },
  shim: {
      d3: { exports: 'd3'},
      nvd3: { exports: 'nv' },
      dimplejs: { exports: 'dimple' },
      crossfilter: { exports: 'crossfilter' },
      dcjs: { exports: 'dc' }
  }
});

require(['d3'], function(d3) {
  window.d3 = d3;
  require(['nvd3', 'dimplejs', 'crossfilter'], function(nv, dimple, crossfilter) {
      window.nv = nv;
      window.dimple = dimple;
      window.crossfilter = crossfilter;
      require(['dcjs'], function(dc) {
        window.dc = dc;
      });
  })
})

