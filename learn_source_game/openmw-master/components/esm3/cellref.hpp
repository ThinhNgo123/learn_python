#ifndef OPENMW_ESM_CELLREF_H
#define OPENMW_ESM_CELLREF_H

#include <cstdint>
#include <string>

#include "components/esm/defs.hpp"
#include "components/esm/refid.hpp"

namespace ESM
{
    class ESMWriter;
    class ESMReader;

    using RefNum = ESM::FormId;

    /* Cell reference. This represents ONE object (of many) inside the
    cell. The cell references are not loaded as part of the normal
    loading process, but are rather loaded later on demand when we are
    setting up a specific cell.
    */

    class CellRef
    {
    public:
        static constexpr std::string_view getRecordType() { return "CellRef"; }

        // Reference number
        // Note: Currently unused for items in containers
        RefNum mRefNum;

        ESM::RefId mRefID; // ID of object being referenced

        float mScale; // Scale applied to mesh

        // The NPC that owns this object (and will get angry if you steal it)
        ESM::RefId mOwner;

        // Name of a global variable. If the global variable is set to '1', using the object is temporarily allowed
        // even if it has an Owner field.
        // Used by bed rent scripts to allow the player to use the bed for the duration of the rent.
        std::string mGlobalVariable;

        // ID of creature trapped in this soul gem
        ESM::RefId mSoul;

        // The faction that owns this object (and will get angry if
        // you take it and are not a faction member)
        ESM::RefId mFaction;

        // PC faction rank required to use the item. Sometimes is -1, which means "any rank".
        int32_t mFactionRank;

        // For weapon or armor, this is the remaining item health.
        // For tools (lockpicks, probes, repair hammer) it is the remaining uses.
        // For lights it is remaining time.
        // This could be -1 if the charge was not touched yet (i.e. full).
        union
        {
            int32_t mChargeInt; // Used by everything except lights
            float mChargeFloat; // Used only by lights
        };
        float mChargeIntRemainder; // Fractional part of mChargeInt

        // Remaining enchantment charge. This could be -1 if the charge was not touched yet (i.e. full).
        float mEnchantmentCharge;

        int32_t mCount;

        // For doors - true if this door teleports to somewhere else, false
        // if it should open through animation.
        bool mTeleport;

        // Teleport location for the door, if this is a teleporting door.
        Position mDoorDest;

        // Destination cell for doors (optional)
        std::string mDestCell;

        // Lock level for doors and containers
        int32_t mLockLevel;
        bool mIsLocked{};
        ESM::RefId mKey, mTrap; // Key and trap ID names, if any

        // This corresponds to the "Reference Blocked" checkbox in the construction set,
        // which prevents editing that reference.
        // -1 is not blocked, otherwise it is blocked.
        signed char mReferenceBlocked;

        // Position and rotation of this object within the cell
        Position mPos;

        /// Calls loadId and loadData
        void load(ESMReader& esm, bool& isDeleted, bool wideRefNum = false);

        void loadId(ESMReader& esm, bool wideRefNum = false);

        /// Implicitly called by load
        void loadData(ESMReader& esm, bool& isDeleted);

        void save(ESMWriter& esm, bool wideRefNum = false, bool inInventory = false, bool isDeleted = false) const;

        void blank();
    };

    void skipLoadCellRef(ESMReader& esm, bool wideRefNum = false);
}

#endif
