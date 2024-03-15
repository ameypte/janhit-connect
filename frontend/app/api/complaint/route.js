
import { NextResponse } from "next/server";
import { query } from "@/app/lib/db";

export const POST = async (req, res) => {
  const data = await req.json();

  console.log(data);
  const raisedBy = data.id;
  const complaint = data.description;
  const summary = "summary";
  const category = "category";
  const tags = "tags";
  const wardno = data.wardno;
  const status = "status";
  console.log(raisedBy, complaint, summary, category, tags, wardno, status);
  try {
    const complaints = await query({
      query:
        "INSERT INTO complaint (raisedby,complaint,summary,category,tags,wardno,status) VALUES (?,?,?,?,?,?,?)",
      values: [raisedBy, complaint,summary, category, tags, wardno, status],
    });

    if (complaints) {
      return NextResponse.json({ complaints: complaints }, { status: 200 });
    }
  } catch (e) {
    console.log(e.message);
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
