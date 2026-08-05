import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { LegacyPage } from "@/src/components/legacy-page";
import { getPageByRoute, getStaticSlugParams, normalizeRoute } from "@/src/lib/page-data";

export const dynamicParams = false;
export const dynamic = "force-static";

export function generateStaticParams() {
  return getStaticSlugParams();
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string[] }> }): Promise<Metadata> {
  const { slug } = await params;
  const route = normalizeRoute(slug);
  const page = getPageByRoute(route);
  if (!page) return {};
  return {
    title: page.title.replace(/ \| Data Learning Hub$/, ""),
    description: page.description,
    alternates: { canonical: route },
    openGraph: { title: page.title, description: page.description, url: route, images: ["/assets/icons/social-card.svg"] },
  };
}

export default async function DynamicPage({ params }: { params: Promise<{ slug: string[] }> }) {
  const { slug } = await params;
  const page = getPageByRoute(normalizeRoute(slug));
  if (!page) notFound();
  return <LegacyPage page={page} />;
}
