"use strict";(self.webpackChunkjupyterlab_myst=self.webpackChunkjupyterlab_myst||[]).push([[5668],{55668:(t,e,r)=>{r.r(e),r.d(e,{gridDirective:()=>n});const n={name:"grid",arg:{type:String},body:{type:"myst",required:!0},run:t=>[{type:"grid",columns:i(t.arg),children:t.body}]};function i(t){const e=(null!=t?t:"1 2 2 3").split(/\s/).map((t=>Number(t.trim()))).filter((t=>!Number.isNaN(t))).map((t=>Math.min(Math.max(Math.floor(t),1),12)));return 0===e.length||e.length>4?[1,2,2,3]:e}}}]);