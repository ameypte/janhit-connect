// get req res ingredients api
import { NextResponse } from "next/server";
import { query } from "@/app/lib/db";

export const POST = async (req, res) => {
  const data = await req.json();

  console.log(data);
  const raisedBy = data.raisedby;
  const complaint = data.complaint;
  const summary = data.summary;
  const category = data.category;
  const tags = data.tags.join(",");
  const wardno = data.wardno;
  const status = data.status;
  console.log(raisedBy, complaint, summary, category, tags, wardno, status);
  try {
    const complaints = await query({
      query:
        "INSERT INTO complaint (raisedby,complaint,summary,category,tags,wardno,status) VALUES (?,?,?,?,?,?,?)",
      values: [raisedBy, complaint, summary, category, tags, wardno, status],
    });

    if (complaints) {
      return NextResponse.json({ complaints: complaints }, { status: 200 });
    }
  } catch (e) {
    return NextResponse.json(
      { message: "Error in Inserting Data" },
      { status: 400 }
    );
  }
};

export const GET = async (req, res) => {
  console.log("Hellow");
  return NextResponse.json({ message: "Hello" }, { status: 400 });
};
