/*
  Copyright (C) 2020 cc9cii

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

  cc9cii cc9c@iinet.net.au

  Much of the information on the data structures are based on the information
  from Tes4Mod:Mod_File_Format and Tes5Mod:File_Formats but also refined by
  trial & error.  See http://en.uesp.net/wiki for details.

  Also see https://tes5edit.github.io/fopdoc/ for FO3/FONV specific details.

*/
#include "loadimod.hpp"

#include <stdexcept>

#include "reader.hpp"
//#include "writer.hpp"

void ESM4::ItemMod::load(ESM4::Reader& reader)
{
    mId = reader.getFormIdFromHeader();
    mFlags = reader.hdr().record.flags;

    while (reader.getSubRecordHeader())
    {
        const ESM4::SubRecordHeader& subHdr = reader.subRecordHeader();
        switch (subHdr.typeId)
        {
            case ESM4::SUB_EDID:
                reader.getZString(mEditorId);
                break;
            case ESM4::SUB_FULL:
                reader.getLocalizedString(mFullName);
                break;
            case ESM4::SUB_MODL:
                reader.getZString(mModel);
                break;
            case ESM4::SUB_MODB:
                reader.get(mBoundRadius);
                break;
            case ESM4::SUB_DESC:
                reader.getLocalizedString(mText);
                break;
            case ESM4::SUB_ICON:
                reader.getZString(mIcon);
                break;
            case ESM4::SUB_MICO:
                reader.getZString(mMiniIcon);
                break;
            case ESM4::SUB_SCRI:
                reader.getFormId(mScriptId);
                break;
            case ESM4::SUB_YNAM:
                reader.getFormId(mPickUpSound);
                break;
            case ESM4::SUB_ZNAM:
                reader.getFormId(mDropSound);
                break;
            case ESM4::SUB_DATA:
                reader.get(mData.mValue);
                reader.get(mData.mWeight);
                break;
            case ESM4::SUB_OBND:
            case ESM4::SUB_MODT: // Model data
            case ESM4::SUB_MODS:
            case ESM4::SUB_MODD: // Model data end
            case ESM4::SUB_DAMC: // Destructible
            case ESM4::SUB_DEST:
            case ESM4::SUB_DMDC:
            case ESM4::SUB_DMDL:
            case ESM4::SUB_DMDT:
            case ESM4::SUB_DMDS:
            case ESM4::SUB_DSTA:
            case ESM4::SUB_DSTD:
            case ESM4::SUB_DSTF: // Destructible end
                reader.skipSubRecordData();
                break;
            default:
                throw std::runtime_error("ESM4::IMOD::load - Unknown subrecord " + ESM::printName(subHdr.typeId));
        }
    }
}

// void ESM4::ItemMod::save(ESM4::Writer& writer) const
//{
// }

// void ESM4::ItemMod::blank()
//{
// }
