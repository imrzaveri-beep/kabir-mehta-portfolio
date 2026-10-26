import {notFound} from 'next/navigation';
import {About,Work,CaseStudy,Services,Process,Playground,Writing,Resume,Testimonials,Contact,Privacy} from '@/components/pages';
import {routes,cases,meta,SITE} from '@/lib/data';
export function generateStaticParams(){return routes.map(r=>({slug:r.split('/')}))}
export const dynamicParams=false;
export async function generateMetadata({params}){const {slug}=await params;const key=slug.join('/');const c=cases.find(c=>key==='work/'+c.slug);const m=c?[c.name+': '+c.title,c.description+' Fictional demo case study.']:meta[key];if(!m)return {};return {title:m[0],description:m[1],alternates:{canonical:SITE+'/'+key+'/'},openGraph:{title:m[0]+' | Kabir Mehta',description:m[1],url:SITE+'/'+key+'/',images:[SITE+'/images/og-'+(c?c.slug:'home')+'.png']}}}
export default async function Page({params}){const {slug}=await params;const key=slug.join('/');const c=cases.find(c=>key==='work/'+c.slug);if(c)return <CaseStudy item={c}/>;const pages={about:About,work:Work,services:Services,process:Process,playground:Playground,writing:Writing,resume:Resume,testimonials:Testimonials,contact:Contact,privacy:Privacy};const Component=pages[key];if(!Component)notFound();return <Component/>}
