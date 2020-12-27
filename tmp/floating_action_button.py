import panel as pn
import numpy as np
import holoviews as hv

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
pn.extension()

template = """
{% extends base %}

{% block postamble %}
    <script type="module" src="https://cdn.jsdelivr.net/npm/@ionic/core/dist/ionic/ionic.esm.js"></script>
    <script nomodule src="https://cdn.jsdelivr.net/npm/@ionic/core/dist/ionic/ionic.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@ionic/core/css/ionic.bundle.css"/>
{% endblock %}

{% block contents %}


<div class="container">

                  <ion-header>
              <ion-toolbar>
                <ion-title>{{ app_title }}</ion-title>
              </ion-toolbar>
            </ion-header>



   <ion-segment>
    <ion-segment-button value="camera">
      <ion-icon name="camera"></ion-icon>
    </ion-segment-button>
    <ion-segment-button value="bookmark">
      <ion-icon name="bookmark"></ion-icon>
    </ion-segment-button>
  </ion-segment>
</ion-toolbar>



<div style="height:78vh">
       {{ embed(roots.A) }}
</div>



            <ion-content color="light">
  <!-- fab placed in the center of the content with a list on each side -->
  <ion-fab vertical="center" horizontal="end" slot="fixed">
  <ion-fab-button color="danger">
  <ion-icon name="share"></ion-icon>
  </ion-fab-button>
  <ion-fab-list side="top">
      <ion-fab-button><ion-icon name="logo-facebook"></ion-icon></ion-fab-button>
  </ion-fab-list>



  <ion-fab-list side="start">
      <ion-fab-button><ion-icon name="logo-whatsapp" onclick=Whatsapp()></ion-icon></ion-fab-button>
      <ion-fab-button><ion-icon name="logo-twitter"></ion-icon></ion-fab-button>
      <ion-fab-button><ion-icon name="logo-facebook"></ion-icon></ion-fab-button>
      <ion-fab-button><ion-icon name="logo-twitter"></ion-icon></ion-fab-button>
      <ion-fab-button><ion-icon name="logo-facebook"></ion-icon></ion-fab-button>
  </ion-fab-list>
  <ion-fab-list side="end">
      <ion-fab-button><ion-icon name="logo-twitter"></ion-icon></ion-fab-button>
      <ion-fab-button><ion-icon name="logo-facebook"></ion-icon></ion-fab-button>
  </ion-fab-list>
  </ion-fab>
 </ion-content>




<ion-footer mode='md'>
  <ion-toolbar>
    <ion-title>Footer</ion-title>


                        <ion-tabs>

                      <ion-tab tab="tab-schedule">
                        <ion-nav> holaaa</ion-nav>
                      </ion-tab>

                      <ion-tab tab="tab-speaker">
                        <ion-nav> cinii </ion-nav>
                      </ion-tab>

                      <ion-tab tab="tab-map" component="page-map">
                        <ion-nav>estas </ion-nav>
                      </ion-tab>

                      <ion-tab tab="tab-about" component="page-about">
                        <ion-nav>todo </ion-nav>
                      </ion-tab>

                      <ion-tab-bar slot="bottom">

                        <ion-tab-button tab="tab-schedule">
                          <ion-icon name="calendar"></ion-icon>
                          <ion-label>Schedule</ion-label>
                          <ion-badge>45</ion-badge>
                        </ion-tab-button>

                        <ion-tab-button tab="tab-speaker">
                          <ion-icon name="person-circle"></ion-icon>
                          <ion-label>Speakers</ion-label>
                        </ion-tab-button>

                        <ion-tab-button tab="tab-map">
                          <ion-icon name="map"></ion-icon>
                          <ion-label>Map</ion-label>
                        </ion-tab-button>

                        <ion-tab-button tab="tab-about">
                          <ion-icon name="information-circle"></ion-icon>
                          <ion-label>About</ion-label>
                        </ion-tab-button>

                      </ion-tab-bar>

                    </ion-tabs>


  </ion-toolbar>
</ion-footer>



<script>

function Whatsapp(){
console.log('pressing Whatsapp button')
}

const segments = document.querySelectorAll('ion-segment')
for (let i = 0; i < segments.length; i++) {
  segments[i].addEventListener('ionChange', (ev) => {
    console.log('se selecciono:', ev.detail['value']);
  })
}
</script>



</div>
{% endblock %}
"""

tmpl = pn.Template(template)

tmpl.add_variable('app_title', '<h1>Custom Template App</h1>')
#
cds = ColumnDataSource(dict(x=[5,4,8],y=[3,8,1]))
p = figure()
p.circle(x='x',y='y',source=cds)

p.xaxis.axis_label = 'Time'
# p.xaxis.axis_label.
p.yaxis.axis_label = 'Position'

pane = pn.pane.panel(p,sizing_mode='stretch_both')
tmpl.add_panel('A', pane)

tmpl.show()