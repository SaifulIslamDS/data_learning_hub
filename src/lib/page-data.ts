import fs from "node:fs";
import path from "node:path";

export type LegacyPageData = {
  route: string;
  title: string;
  description: string;
  canonical: string;
  bodyAttrs: Record<string, string | string[]>;
  mainHtml: string;
  scripts: string[];
  inlineScripts: string[];
};

type RouteRecord = {
  file: string;
  title: string;
  description: string;
  canonical: string;
  bodyAttrs: Record<string, string | string[]>;
  scripts: string[];
};

const generatedRoot = path.join(process.cwd(), "src", "generated");
const manifestPath = path.join(generatedRoot, "routes.json");

let routeCache: Record<string, RouteRecord> | null = null;
const pageCache = new Map<string, LegacyPageData>();

export function getRouteManifest(): Record<string, RouteRecord> {
  if (!routeCache) {
    routeCache = JSON.parse(fs.readFileSync(manifestPath, "utf8")) as Record<string, RouteRecord>;
  }
  return routeCache;
}

export function normalizeRoute(parts: string[] = []): string {
  return parts.length === 0 ? "/" : `/${parts.join("/")}/`;
}

export function getPageByRoute(route: string): LegacyPageData | null {
  const cached = pageCache.get(route);
  if (cached) return cached;
  const record = getRouteManifest()[route];
  if (!record) return null;
  const filePath = path.join(generatedRoot, "pages", record.file);
  const page = JSON.parse(fs.readFileSync(filePath, "utf8")) as LegacyPageData;
  pageCache.set(route, page);
  return page;
}

export function getStaticSlugParams(): Array<{ slug: string[] }> {
  return Object.keys(getRouteManifest())
    .filter((route) => route !== "/" && route !== "/404/" && route !== "/offline/")
    .map((route) => ({ slug: route.split("/").filter(Boolean) }));
}
