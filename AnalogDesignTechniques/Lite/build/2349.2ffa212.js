"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[2349,4954],{89067:(e,t,r)=>{r.r(t),r.d(t,{IServiceWorkerManager:()=>u,JupyterLiteServer:()=>h,Router:()=>a,ServiceWorkerManager:()=>_,WORKER_NAME:()=>d});var i=r(50558),s=r(41830),n=r(2159),o=r(44700);class a{constructor(){this._routes=[]}get(e,t){this._add("GET",e,t)}put(e,t){this._add("PUT",e,t)}post(e,t){this._add("POST",e,t)}patch(e,t){this._add("PATCH",e,t)}delete(e,t){this._add("DELETE",e,t)}async route(e){const t=new URL(e.url),{method:r}=e,{pathname:i}=t;for(const s of this._routes){if(s.method!==r)continue;const n=i.match(s.pattern);if(!n)continue;const o=n.slice(1);let a;if("PATCH"===s.method||"PUT"===s.method||"POST"===s.method)try{a=JSON.parse(await e.text())}catch{a=void 0}return s.callback.call(null,{pathname:i,body:a,query:Object.fromEntries(t.searchParams)},...o)}throw new Error("Cannot route "+e.method+" "+e.url)}_add(e,t,r){"string"==typeof t&&(t=new RegExp(t)),this._routes.push({method:e,pattern:t,callback:r})}}class c{constructor(e){this._isDisposed=!1,this._serverSettings=e.serverSettings,this._stream=new n.Stream(this)}async emit({data:e,schema_id:t}){this._stream.emit({...e,schema_id:t})}dispose(){this.isDisposed||(this._isDisposed=!0,n.Signal.clearData(this),this._stream.stop())}get isDisposed(){return this._isDisposed}get stream(){return this._stream}get serverSettings(){return this._serverSettings}}class h extends s.Application{constructor(e){var t;super(e),this.name="JupyterLite Server",this.namespace=this.name,this.version="unknown",this._router=new a;const r={...i.ServerConnection.makeSettings(),WebSocket:o.WebSocket,fetch:null!==(t=this.fetch.bind(this))&&void 0!==t?t:void 0};this._serviceManager=new i.ServiceManager({standby:"never",serverSettings:r,events:new c({serverSettings:r})})}get router(){return this._router}get serviceManager(){return this._serviceManager}async fetch(e,t){if(!(e instanceof Request))throw Error("Request info is not a Request");return this._router.route(e)}attachShell(e){}evtResize(e){}registerPluginModule(e){let t=e.default;Object.prototype.hasOwnProperty.call(e,"__esModule")||(t=e),Array.isArray(t)||(t=[t]),t.forEach((e=>{try{this.registerPlugin(e)}catch(e){console.error(e)}}))}registerPluginModules(e){e.forEach((e=>{this.registerPluginModule(e)}))}}var l=r(21961);const g=r.p+"service-worker.js",u=new l.Token("@jupyterlite/server-extension:IServiceWorkerManager"),d=`${g}`.split("/").slice(-1)[0];var v=r(64145);const p=v.PageConfig.getOption("appVersion");class _{constructor(e){var t;this.unregisterOldServiceWorkers=async e=>{const t=`${e}-version`,r=localStorage.getItem(t);if(r&&r!==p||!r){console.info("New version, unregistering existing service workers.");const e=await navigator.serviceWorker.getRegistrations();await Promise.all(e.map((e=>e.unregister()))),console.info("All existing service workers have been unregistered.")}localStorage.setItem(t,p)},this._pingServiceWorker=async()=>{const e=await fetch("/api/service-worker-heartbeat");"ok"===await e.text()&&setTimeout(this._pingServiceWorker,2e4)},this._registration=null,this._registrationChanged=new n.Signal(this),this._ready=new l.PromiseDelegate;const r=null!==(t=null==e?void 0:e.workerUrl)&&void 0!==t?t:v.URLExt.join(v.PageConfig.getBaseUrl(),d),i=new URL(r,window.location.href),s=v.PageConfig.getOption("enableServiceWorkerCache")||"false";i.searchParams.set("enableCache",s),this.initialize(i.href).catch(console.warn)}get registrationChanged(){return this._registrationChanged}get enabled(){return null!==this._registration}get ready(){return this._ready.promise}async initialize(e){const{serviceWorker:t}=navigator;let r=null;if(t){if(t.controller){const e=t.controller.scriptURL;await this.unregisterOldServiceWorkers(e),r=await t.getRegistration(e)||null,console.info("JupyterLite ServiceWorker was already registered")}}else console.warn("ServiceWorkers not supported in this browser");if(!r&&t)try{console.info("Registering new JupyterLite ServiceWorker",e),r=await t.register(e),console.info("JupyterLite ServiceWorker was sucessfully registered")}catch(e){console.warn(e),console.warn(`JupyterLite ServiceWorker registration unexpectedly failed: ${e}`)}this._setRegistration(r),r?(this._ready.resolve(void 0),setTimeout(this._pingServiceWorker,2e4)):this._ready.reject(void 0)}_setRegistration(e){this._registration=e,this._registrationChanged.emit(this._registration)}}}}]);
//# sourceMappingURL=2349.2ffa212.js.map