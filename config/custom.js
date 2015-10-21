require.config({
  paths: {
      d3: '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min',
      nvd3: '//cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.1/nv.d3.min',
      dimplejs: '//cdnjs.cloudflare.com/ajax/libs/dimple/2.1.6/dimple.latest.min'
  },
  shim: {
      d3: { exports: 'd3'},
      nvd3: { exports: 'nv' },
      dimplejs: { exports: 'dimple' }
  }
});

require(['d3'], function(d3) {
  window.d3 = d3;
  require(['nvd3', 'dimplejs'], function(nv, dimple) {
      window.nv = nv;
      window.dimple = dimple;
  })
})

