import React from "react";
import Navbar from "../components/user/navbar";
import Head from "next/head";
import Hero from "../components/hero";
import SectionTitle from "../components/sectionTitle";
import Benefits from "../components/benefits";
import Video from "../components/video";
import Faq from "../components/faq";
import Footer from "../components/footer";
import PopupWidget from "../components/popupWidget";
import { benefitOne } from "../components/data";
// import { benefitTwo } from "../components/data";

export default function page() {
  return (
    <div>
      <>
        <Head>
          <title>Janhit - Adressing the peoples</title>
          <meta
            name="description"
            content="Nextly is a free lanith next.js & Tailwind CSS"
          />
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <Navbar />
        <Hero />
        <SectionTitle title=" Why should you use जनहित Connect">
          Choose JanhitConnect for effortless solutions to all your problems,
          making community issues a thing of the past. With a user-centric
          approach, we simplify life for everyone, ensuring a brighter tomorrow
          for all.
        </SectionTitle>
        <Benefits data={benefitOne} />
        <SectionTitle
          pretitle="Watch a video"
          title="Learn how to use जनहित Connect "
        ></SectionTitle>
        <Video />
        {/* <SectionTitle
        pretitle="Testimonials"
        title="Here's what our customers said"
      >
        Testimonails is a great way to increase the brand trust and awareness.
        Use this section to highlight your popular customers.
      </SectionTitle>
      <Testimonials />
      */}
        <SectionTitle pretitle="FAQ" title="Frequently Asked Questions">
          Answer your customers possible questions here, it will increase the
          conversion rate as well as support or chat requests.
        </SectionTitle>
        <Faq />
        {/* <Cta /> */}
        <Footer />
        <PopupWidget />
      </>
    </div>
  );
}
