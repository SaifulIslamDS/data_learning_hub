import { notFound } from "next/navigation";
import { LegacyPage } from "@/src/components/legacy-page";
import { getPageByRoute } from "@/src/lib/page-data";

export default function HomePage() {
  const page = getPageByRoute("/");
  if (!page) notFound();
  return <LegacyPage page={page} />;
}
